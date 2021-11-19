import { SuccessPage } from './../success/success.page';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CheckoutPage } from './checkout.page';

const routes: Routes = [
	{
		path: '',
		component: CheckoutPage
	},
	{
		path: '/success',
		component: SuccessPage
	}
];

@NgModule({
	imports: [RouterModule.forChild(routes)],
	exports: [RouterModule]
})
export class CheckoutPageRoutingModule {}
