import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-mat-card',
  standalone: true,
  imports: [CommonModule, MatCardModule],
  templateUrl: './app-mat-card.component.html',
  styleUrls: ['./app-mat-card.component.scss']
})
export class AppMatCardComponent {
  @Input() title = '';
  @Input() subtitle = '';
}
