import { Injectable } from "@angular/core";
import { ThemePalette } from "@angular/material/core";
import { BehaviorSubject } from "rxjs";

@Injectable({
  providedIn: 'root'
})

export class MainService {
  // Create Observable for color theme
  public colorThemeStore = new BehaviorSubject<ThemePalette | 'success'>('primary');
  colorTheme$ = this.colorThemeStore.asObservable();

  setColorTheme(theme: ThemePalette | 'success'): void {
    console.log(theme)
    this.colorThemeStore.next(theme);
  }
}
