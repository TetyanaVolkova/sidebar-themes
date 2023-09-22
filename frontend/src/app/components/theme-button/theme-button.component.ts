import { Component, HostBinding, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { CdkDrag, CdkDragHandle } from '@angular/cdk/drag-drop';
import { ThemePalette } from '@angular/material/core';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-theme-button',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatIconModule,
    CdkDrag,
    CdkDragHandle
  ],
  templateUrl: './theme-button.component.html',
  styleUrls: ['./theme-button.component.scss']
})
export class ThemeButtonComponent {
  @Input() type: ThemePalette = 'primary';
  @HostBinding('class')
  get hostClass() {
    return `${this.type}-theme`
  };

  themeColor: 'primary' | 'accent' | 'warn' = 'warn';
  isDark = false;

  toggleTheme(event: any): void {
    event.preventDefault();
    this.isDark = !this.isDark;
    if (this.isDark) {
      document.body.classList.add('dark-theme');
      document.getElementById('nav_container')?.classList.add('dark-theme');
      document.getElementsByClassName('sidenav-container')[0].classList.add('dark-theme');
      document.getElementById('position_fixed')?.classList.add('dark-theme');
    } else {
      document.body.classList.remove('dark-theme');
      document.getElementById('nav_container')?.classList.remove('dark-theme');
      document.getElementsByClassName('sidenav-container')[0].classList.remove('dark-theme');
      document.getElementById('position_fixed')?.classList.remove('dark-theme');
    }
  }

}
