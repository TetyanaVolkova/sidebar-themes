import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },
  {
    path: 'dashboard',
    loadComponent: () => import('./components/dashboard/dashboard.component').then(com => com.DashboardComponent)
  },
  {
    path: 'reports',
    loadComponent: () => import('./components/stats-reports/stats-reports.component').then(com => com.StatsReportsComponent)
  },
  {
    path: 'contacts',
    loadComponent: () => import('./components/contacts/contacts.component').then(com => com.ContactsComponent)
  },
  {
    path: 'surveys',
    loadComponent: () => import('./components/surveys/surveys.component').then(com => com.SurveysComponent)
  },
  {
    path: 'activities',
    loadComponent: () => import('./components/activities/activities.component').then(com => com.ActivitiesComponent)
  },
  {
    path: 'issues',
    loadComponent: () => import('./components/issues/issues.component').then(com => com.IssuesComponent)
  }
];

export class AppRoutingModule { }
