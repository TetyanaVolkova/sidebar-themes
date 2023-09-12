import { Component } from '@angular/core';
import { AppMatCardComponent } from '../app-mat-card/app-mat-card.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
  standalone: true,
  imports: [ AppMatCardComponent ]
})
export class DashboardComponent {

}
