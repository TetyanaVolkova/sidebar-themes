import { Component, HostBinding, Input } from '@angular/core';
import { CommonModule, NgIf } from '@angular/common';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { RouterModule } from '@angular/router';

import { MatSidenavModule} from '@angular/material/sidenav';
import { MatRadioModule } from '@angular/material/radio';
import { MatButtonModule } from '@angular/material/button';

import { ResizableModule, ResizeEvent } from 'angular-resizable-element';
import { NavComponent } from './components/nav/nav.component';
import { ThemeButtonComponent } from './components/theme-button/theme-button.component';
import { ThemePalette } from '@angular/material/core';

import { environment } from 'src/environments/environment';

// Import Census AAS package
import CensusAas  from '@census/vanilla-aas';
import { UserInfoComponent } from './components/user-info/user-info.component';

const censusAas = new CensusAas({
  baseUrl: environment.baseUrl,
  authRedirectUrl: environment.redirectUrl,
});
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true,
  imports: [
    CommonModule,
    NgIf,
    MatSidenavModule,
    MatButtonModule,
    MatRadioModule,
    FormsModule,
    ReactiveFormsModule,
    ResizableModule,
    RouterModule,
    NavComponent,
    ThemeButtonComponent,
    UserInfoComponent
  ],
})
export class AppComponent {

  @Input() type: ThemePalette = 'warn';
  @HostBinding('class')
  get hostClass() {
    return `${this.type}-root`
  };

  resizeStyle: object = {};
  isOpen_YourVariable = true;

 constructor() {
    // censusAas.getUser(function (err: any, response: any) {
    //   if(err) {
    //     return;
    //   }
    //   console.log(response);
    // });
 }
  /**
    * Finalizes resize positions
    * (used for drawer/sidenav width)
    * @param event
    */
  onResizeEnd(event: ResizeEvent): void {
    const userInfo = document.getElementById('user_info_container');
    console.log(event)
    if(event.rectangle.right < 220 && event.edges.right as number < 0) {
      this.resizeStyle = {
        left: `0px`,
        width: `70px`,
      };
    userInfo?.classList.add('small_image');
      return;
    }
    if(event.rectangle.right < 220 && event.edges.right as number > 0) {
      this.resizeStyle = {
        left: `0px`,
        width: `220px`,
      };
      userInfo?.classList.remove('small_image');
      return;
    }
    this.resizeStyle = {
      left: `${event.rectangle.left}px`,
      width: `${event.rectangle.width}px`,
    };
  };
}
