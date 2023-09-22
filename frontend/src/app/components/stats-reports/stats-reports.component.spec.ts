import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatsReportsComponent } from './stats-reports.component';

describe('StatsReportsComponent', () => {
  let component: StatsReportsComponent;
  let fixture: ComponentFixture<StatsReportsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [StatsReportsComponent]
    });
    fixture = TestBed.createComponent(StatsReportsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
