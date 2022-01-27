import { Component, OnDestroy, OnInit } from '@angular/core';
import { Writing } from 'src/app/models/writing';
import { DataService } from '../data.service';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-writing',
  templateUrl: './writing.component.html',
  styleUrls: ['./writing.component.scss'],
  providers: [DataService]
})
export class WritingComponent implements OnInit, OnDestroy {

  writing: Writing;
  id: string;
  prevLimit: number;
  prevOffset: number;

  subscription: Subscription;

  constructor(
    private activatedRoute: ActivatedRoute, 
    private router: Router,
    private dataService: DataService) {}

  ngOnInit() {
    this.subscription = this.activatedRoute.paramMap.subscribe(params => {
      this.id = params.get('id');
      this.dataService.getWriting(this.id).subscribe(item => this.writing = item);
    });
  }  

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  onBack() {
    this.router.navigate(['.'], { relativeTo: this.activatedRoute.parent, queryParams: { limit: this.prevLimit, offset: this.prevOffset } });
  }
}
