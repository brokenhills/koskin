import { Component, OnInit, Input } from '@angular/core';
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

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getWritings()
    .subscribe(writings => {
      this.writings = writings;
    });
  }
}
