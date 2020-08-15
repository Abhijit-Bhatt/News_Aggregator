import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http'

import { FormsModule } from '@angular/forms'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatInputModule} from '@angular/material/input';
import { OptionsComponent } from './options/options.component';
import { DisplayNewsComponent } from './options/display-news/display-news.component'

import {MatCardModule, MatCard} from '@angular/material/card';
import { FeedComponent } from './feed/feed.component';
import { WelcomeComponent } from './welcome/welcome.component'

import {MatExpansionModule} from '@angular/material/expansion';
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import { SettingsComponent } from './settings/settings.component';

import {MatSidenavModule} from '@angular/material/sidenav';

import {MatSelectModule} from '@angular/material/select'

import {ReactiveFormsModule} from '@angular/forms'


@NgModule({
  declarations: [
    AppComponent,
    OptionsComponent,
    DisplayNewsComponent,
    FeedComponent,
    WelcomeComponent,
    SettingsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    FormsModule,
    HttpClientModule,
    MatCardModule,
    MatExpansionModule,
    MatIconModule,
    MatDividerModule,
    MatSidenavModule,
    MatSelectModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
