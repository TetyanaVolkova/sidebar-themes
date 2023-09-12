import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppMatCardComponent } from '../app-mat-card/app-mat-card.component';

@Component({
  selector: 'app-activities',
  standalone: true,
  imports: [CommonModule, AppMatCardComponent],
  templateUrl: './activities.component.html',
  styleUrls: ['./activities.component.scss']
})
export class ActivitiesComponent {

}
