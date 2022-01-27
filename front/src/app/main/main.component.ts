import { HttpParams } from '@angular/common/http';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { DataService } from '../data.service';
import { HelperService } from '../helper.service';
import { MainInfo } from '../models/mainInfo';
import { Writing } from '../models/writing';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss'],
  providers: [DataService]
})
export class MainComponent implements OnInit, OnDestroy {

  DEFAULT_LIMIT: number = 10;

  mainItems: MainInfo[] = [];
  writings: Writing[] = [];
  limit: number = this.DEFAULT_LIMIT;
  offset: number = 0;
  contentLength: number;
  isShowList: boolean = true;

  subscription: Subscription;

  constructor(
    private activatedRoute: ActivatedRoute, 
    private dataService: DataService, 
    private helper: HelperService) {}

  ngOnInit(): void {
    this.subscription = this.activatedRoute.paramMap.subscribe(() => {
      this.dataService
        .getMainItems(this.limit.toString(), this.offset.toString())
          .subscribe(items => this.mainItems = items);
      this.dataService
        .getWritings(new HttpParams().set('limit', this.limit.toString()).set('offset', this.offset.toString()).set('is_liked', true))
          .subscribe(items => this.writings = items['results']);
    });
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  getShortContent(fullContent: string): string {
    const { content, length } = this.helper.getShortContent(fullContent);
    this.contentLength = length;
    return content;
  }

  onActivateItem() {
    this.isShowList = false;
  }

  onDeactivateItem() {
    this.isShowList = true;
  }
  
}
