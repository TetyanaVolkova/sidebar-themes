import { Component, HostBinding, Input } from '@angular/core';

import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';

import { RouterModule } from '@angular/router';
import { ThemePalette } from '@angular/material/core';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss'],
  standalone: true,
  imports: [
    RouterModule,
    MatIconModule,
    MatCardModule
  ]
})
export class NavComponent {
  @Input() type: ThemePalette | 'success' = 'primary';
  @HostBinding('class')
  get hostClass() {
    return `${this.type}-nav`
  }
}
