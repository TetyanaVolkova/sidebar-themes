import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppMatCardComponent } from '../app-mat-card/app-mat-card.component';

@Component({
  selector: 'app-issues',
  standalone: true,
  imports: [CommonModule, AppMatCardComponent],
  templateUrl: './issues.component.html',
  styleUrls: ['./issues.component.scss']
})
export class IssuesComponent {

}
