import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppMatCardComponent } from '../app-mat-card/app-mat-card.component';

@Component({
  selector: 'app-contacts',
  standalone: true,
  imports: [CommonModule, AppMatCardComponent],
  templateUrl: './contacts.component.html',
  styleUrls: ['./contacts.component.scss']
})
export class ContactsComponent {

}
