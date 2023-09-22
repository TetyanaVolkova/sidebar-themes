import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppMatCardComponent } from './app-mat-card.component';

describe('AppMatCardComponent', () => {
  let component: AppMatCardComponent;
  let fixture: ComponentFixture<AppMatCardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [AppMatCardComponent]
    });
    fixture = TestBed.createComponent(AppMatCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
