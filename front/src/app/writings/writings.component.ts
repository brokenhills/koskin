import { HttpParams } from '@angular/common/http';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { DataService } from '../data.service';
import { HelperService } from '../helper.service';
import { Writing } from '../models/writing';

@Component({
  selector: 'app-writings',
  templateUrl: './writings.component.html',
  styleUrls: ['./writings.component.scss'],
  providers: [DataService]
})
export class WritingsComponent implements OnInit, OnDestroy {

  DEFAULT_LIMIT: number = 10;

  writings: Writing[] = [];
  currentWriting: Writing;
  previous: string;
  next: string;
  count: number;
  contentLength: number;
  limit: number;
  offset: number = 0;
  isShowList: boolean = true;

  subscription: Subscription;

  constructor(
    private activatedRoute: ActivatedRoute, 
    private router: Router,
    private dataService: DataService, 
    private helper: HelperService) {}

  ngOnInit() {
    this.subscription = this.activatedRoute.queryParamMap.subscribe(queryParams => {
      this.limit = Number.parseInt(queryParams.get('limit'))||this.DEFAULT_LIMIT;
      this.offset = Number.parseInt(queryParams.get('offset'))||0;
      this.dataService.getWritings(new HttpParams().set('limit', this.limit.toString()).set('offset', this.offset.toString()))
      .subscribe(writings => {
        this.writings = writings['results'];
        this.next = writings['next'];
        this.previous = writings['previous'];
        this.count = writings['count'];
      });
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

  getNextPage(): void {
    this.router.navigate(
      ['writings'], 
      { queryParams: { offset: this.offset += this.DEFAULT_LIMIT||0, limit: this.DEFAULT_LIMIT }}
    );
  }

  getPreviousPage(): void {
    this.router.navigate(
      ['writings'], 
      { queryParams: { offset: this.offset -= this.DEFAULT_LIMIT||0, limit: this.DEFAULT_LIMIT }}
    );
  }

  onActivateItem() {
    this.isShowList = false;
  }

  onDeactivateItem() {
    this.isShowList = true;
  }
}
