import { Component, OnInit, Input } from '@angular/core';
import { Writing } from 'src/app/models/writing';

@Component({
  selector: 'app-writing',
  templateUrl: './writing.component.html',
  styleUrls: ['./writing.component.scss']
})
export class WritingComponent implements OnInit {

  @Input()
  writing: Writing;

  constructor() { }

  ngOnInit() {
  }

}
