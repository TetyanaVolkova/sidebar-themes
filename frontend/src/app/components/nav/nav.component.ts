import { Component, HostBinding, Input, OnInit, OnDestroy } from '@angular/core';
import { AsyncPipe, CommonModule } from '@angular/common';
import { MainService } from 'src/app/services/main.service';

import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';

import { RouterModule } from '@angular/router';
import { ThemePalette } from '@angular/material/core';
import { Subject, takeUntil } from 'rxjs';

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    MatIconModule,
    MatCardModule,
    AsyncPipe
  ],
  providers: [MainService],
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit, OnDestroy {
  destroy$ = new Subject<boolean>();
  @Input() type: ThemePalette | 'success';
  @HostBinding('class')
  get hostClass() {
    return `${this.type}-nav`
  }

  constructor(public mainService: MainService) {}

  ngOnDestroy(): void {
    this.destroy$.next(true);
    this.destroy$.complete();
  }

  ngOnInit(): void {
    this.mainService.colorTheme$
    .pipe(takeUntil(this.destroy$))
      .subscribe((colorTheme) => {
        console.log(colorTheme)
        this.type = colorTheme;
      });
  }
}
