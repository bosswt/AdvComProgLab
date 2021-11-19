import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductsPage } from '../products/products.page';
import { HomePage } from './home.page';

const routes: Routes = [
	{
		path: '',
		component: HomePage
	},
	{
		path: 'products',
		component: ProductsPage
	}
];

@NgModule({
	imports: [RouterModule.forChild(routes)],
	exports: [RouterModule]
})
export class HomePageRoutingModule {}
