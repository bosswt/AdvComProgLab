import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Storage } from '@ionic/storage';
import { Router } from '@angular/router';

@Component({
	selector: 'app-products',
	templateUrl: './products.page.html',
	styleUrls: ['./products.page.scss']
})
export class ProductsPage implements OnInit {
	data: Observable<any>;
	stocks: Array<{ name: string; price: number; qty: number; img: string }>;
	url: string = 'http://localhost:5000/stocks';
	cart: Array<{ name: string; price: number; qty: number; img: string }>;
	check: Array<{ name: string; price: number; qty: number; img: string }>;
	constructor(
		public http: HttpClient,
		private storage: Storage,
		private router: Router
	) {
		this.data = this.http.get(this.url);
		this.data.subscribe((data) => {
			this.stocks = data.data;
			this.cart = JSON.parse(JSON.stringify(data.data));
			this.cart = this.cart.map((product: any) => {
				delete product['img'];
				product['qty'] = 0;
				return product;
			});
		});
	}

	ngOnInit() {}
	ionViewWillEnter() {}

	incrementQty(index: number) {
		if (this.cart[index].qty + 1 <= this.stocks[index].qty)
			this.cart[index].qty += 1;
	}
	decrementQty(index: number) {
		if (this.cart[index].qty - 1 >= 0) this.cart[index].qty -= 1;
	}

	checkout() {
		this.check = this.cart.filter((product) => {
			return product.qty > 0;
		});
		if (this.check.length > 0) {
			this.storage.set('cart', this.check);
			this.router.navigate(['/checkout']);
		}
	}
}
