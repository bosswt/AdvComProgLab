import { Component } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Router } from '@angular/router';

@Component({
	selector: 'app-home',
	templateUrl: 'home.page.html',
	styleUrls: ['home.page.scss']
})
export class HomePage {
	name: string;
	age: number = 15;
	constructor(private storage: Storage, private router: Router) {}
	ionViewWillEnter() {
		this.storage.clear();
	}
	next() {
		if (this.name) {
			this.storage.set('name', this.name);
			this.storage.set('age', this.age);
			this.router.navigate(['/products']);
		}
	}
}
