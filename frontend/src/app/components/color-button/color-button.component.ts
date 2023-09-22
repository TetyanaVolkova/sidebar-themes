import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ThemePalette } from '@angular/material/core';
import { MainService } from 'src/app/services/main.service';

@Component({
  selector: 'app-color-button',
  standalone: true,
  imports: [CommonModule],
  providers: [MainService],
  templateUrl: './color-button.component.html',
  styleUrls: ['./color-button.component.scss']
})
export class ColorButtonComponent {

  constructor(private mainService: MainService) {
    this.mainService.colorTheme$
      .subscribe((colorTheme) => {
        console.log(colorTheme);
      })

  }
  setTheme(theme: ThemePalette | 'success') {
    this.mainService.setColorTheme(theme);
  }
}
