import { HomePage } from './../home/home.page';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SuccessPage } from './success.page';

const routes: Routes = [
	{
		path: '',
		component: SuccessPage
	},
	{
		path: 'home',
		component: HomePage
	}
];

@NgModule({
	imports: [RouterModule.forChild(routes)],
	exports: [RouterModule]
})
export class SuccessPageRoutingModule {}
