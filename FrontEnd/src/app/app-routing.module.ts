import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { OptionsComponent } from './options/options.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { FeedComponent } from './feed/feed.component';
import { SettingsComponent } from './settings/settings.component';


const routes: Routes = [
  {
    path:'welcome',
    component: WelcomeComponent
  },
  {path:'options',
  component: OptionsComponent
  },
  {
    path: 'feed',
    component: FeedComponent
  },
  {
    path: 'settings',
    component: SettingsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
