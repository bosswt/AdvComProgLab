import { OrdersPage } from './orders/orders.page';
import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
	{
		path: 'home',
		loadChildren: () =>
			import('./home/home.module').then((m) => m.HomePageModule)
	},
	{
		path: '',
		redirectTo: 'home',
		pathMatch: 'full'
	},
	{
		path: 'products',
		loadChildren: () =>
			import('./products/products.module').then(
				(m) => m.ProductsPageModule
			)
	},
	{
		path: 'checkout',
		loadChildren: () =>
			import('./checkout/checkout.module').then(
				(m) => m.CheckoutPageModule
			)
	},
	{
		path: 'success',
		loadChildren: () =>
			import('./success/success.module').then((m) => m.SuccessPageModule)
	},
	{
		path: 'orders',
		loadChildren: () =>
			import('./orders/orders.module').then((m) => m.OrdersPageModule)
	},
  {
    path: 'chart',
    loadChildren: () => import('./chart/chart.module').then( m => m.ChartPageModule)
  }
];

@NgModule({
	imports: [
		RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
	],
	exports: [RouterModule]
})
export class AppRoutingModule {}
