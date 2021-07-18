import { Component, OnInit, Input, ChangeDetectionStrategy, OnDestroy } from '@angular/core';
import { DataService } from '../data.service';
import { Writing } from '../models/writing';

@Component({
  selector: 'app-writings',
  templateUrl: './writings.component.html',
  styleUrls: ['./writings.component.scss'],
  providers: [DataService]
})
export class WritingsComponent implements OnInit {

  writings: Writing[] = [];
  currentWriting: Writing;
  previous: string;
  next: string;
  count: number;
  contentLength: number;
  limit: string = '10';
  offset: string = '0'

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getWritings(this.limit, this.offset)
    .subscribe(writings => {
      this.writings = writings['results'];
      this.next = writings['next'];
      this.previous = writings['previous'];
      this.count = writings['count'];
    });
  }

  getShortContent(content: string): string {
    const splitted = content.split(' ');
    this.contentLength = splitted.length;
    if (this.contentLength < 200) {
      return content;
    }
    return splitted.slice(0, 201).join(' ') + '...';
  }
}
