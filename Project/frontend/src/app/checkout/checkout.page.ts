import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Storage } from '@ionic/storage';
import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-checkout',
	templateUrl: './checkout.page.html',
	styleUrls: ['./checkout.page.scss']
})
export class CheckoutPage implements OnInit {
	cart: Array<any>;
	total: number = 0;
	url: string = 'http://localhost:5000/orders';
	body: any = {};
	constructor(
		private storage: Storage,
		private router: Router,
		private http: HttpClient
	) {}
	ionViewWillEnter() {
		this.storage.get('cart').then((data) => {
			this.cart = data;
			this.cart.forEach((product) => {
				this.total += product.qty * product.price;
			});
			this.storage.set('total', this.total);
		});
	}
	ngOnInit() {}
	async confirm() {
		const pr = await Promise.all([
			this.storage.get('name'),
			this.storage.get('age'),
			this.storage.get('cart'),
			this.storage.get('total')
		]);
		this.body.name = pr[0];
		this.body.age = pr[1];
		this.body.cart = pr[2];
		this.body.total = pr[3];
		console.log(this.body);
		this.http
			.post(this.url, this.body, {
				headers: { 'Content-Type': 'application/json' }
			})
			.subscribe((data) => console.log(data));
		this.router.navigate(['/success']);
	}
}
