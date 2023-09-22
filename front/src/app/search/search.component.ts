import { Component, EventEmitter, Output } from '@angular/core';
import { HttpParams } from '@angular/common/http';

import { DataService } from '../data.service';
import { Writing } from '../models/writing';
import { DEFAULT_LIMIT, DEFAULT_OFFSET } from '../constants';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent {

  @Output()
  writings = new EventEmitter<any>();

  constructor(
    private dataService: DataService,
  ) {}

  searchWritings(text) {
    const params = new HttpParams()
      .set('limit', DEFAULT_LIMIT)
      .set('offset', DEFAULT_OFFSET)
    if (text) {
      this.dataService.getWritings(
        params.set('search', text)
      ).subscribe(res => {
        this.writings.emit(res);
      });
    } else {
      this.dataService.getWritings(
        params
      ).subscribe(res => {
        this.writings.emit(res);
      });
    }
  }
}
