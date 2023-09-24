import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ThemePalette } from '@angular/material/core';
import { MainService } from 'src/app/services/main.service';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-color-button',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  templateUrl: './color-button.component.html',
  styleUrls: ['./color-button.component.scss']
})
export class ColorButtonComponent {
  @Input() themeColor: ThemePalette | 'success' = 'primary';
  constructor(private mainService: MainService) {
    this.mainService.colorTheme$
      .subscribe((colorTheme) => {
        console.log(colorTheme);
      })

  }
  setTheme() {
    this.mainService.setColorTheme(this.themeColor);
  }
}
