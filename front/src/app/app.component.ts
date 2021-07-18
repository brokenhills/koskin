import { Component, OnInit } from '@angular/core';
import { DataService } from '../app/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [DataService]
})
export class AppComponent {

  title = 'front';

}
