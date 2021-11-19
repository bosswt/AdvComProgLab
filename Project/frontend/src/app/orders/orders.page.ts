import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-orders',
	templateUrl: './orders.page.html',
	styleUrls: ['./orders.page.scss']
})
export class OrdersPage implements OnInit {
	url: string = 'http://localhost:5000/orders';
	data: Observable<any>;
	orders: any;
	constructor(private http: HttpClient) {
		this.data = this.http.get(this.url);
		this.data.subscribe((data) => {
			this.orders = data.data;
		});
	}

	ngOnInit() {}
}
