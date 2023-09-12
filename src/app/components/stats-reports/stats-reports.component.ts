import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppMatCardComponent } from '../app-mat-card/app-mat-card.component';

@Component({
  selector: 'app-stats-reports',
  standalone: true,
  imports: [CommonModule, AppMatCardComponent],
  templateUrl: './stats-reports.component.html',
  styleUrls: ['./stats-reports.component.scss']
})
export class StatsReportsComponent {

}
