import { Component, EventEmitter, Output } from '@angular/core';
import { HttpParams } from '@angular/common/http';

import { DataService } from '../data.service';
import { Writing } from '../models/writing';
import { DEFAULT_LIMIT, DEFAULT_OFFSET } from '../constants';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.scss']
})
export class FilterComponent {

  @Output()
  writings = new EventEmitter<any>();

  constructor(
    private dataService: DataService,
  ) {}

  filterWritings(key, date) {
    const params = new HttpParams()
      .set('limit', DEFAULT_LIMIT)
      .set('offset', DEFAULT_OFFSET)
    if (date && key) {
      this.dataService.getWritings(
        params.set(key, date)
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

  filterDateAfter(date) {
    this.filterWritings('date_after', date);
  }

  filterDateBefore(date) {
    this.filterWritings('date_before', date);
  }
}
