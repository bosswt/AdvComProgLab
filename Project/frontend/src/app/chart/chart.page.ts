import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Component, OnInit, ViewChild } from '@angular/core';
import { Chart } from 'chart.js';

@Component({
	selector: 'app-chart',
	templateUrl: './chart.page.html',
	styleUrls: ['./chart.page.scss']
})
export class ChartPage implements OnInit {
	@ViewChild('barChart') barChart;
	bars: any;
	colorArray: any;
	data: Observable<any>;
	data2: Observable<any>;
	axis: any;
	stocks: any;
	url: string = 'http://localhost:5000/chart';
	url2: string = 'http://localhost:5000/stocks';
	constructor(private http: HttpClient) {
		this.data = this.http.get(this.url);
		this.data.subscribe((data) => {
			this.axis = data;
		});
		this.data2 = this.http.get(this.url2);
		this.data2.subscribe((data) => {
			this.stocks = data.data;
		});
	}

	ngOnInit() {}
	ionViewDidEnter() {
		this.createBarChart();
		console.log(this.axis);
	}

	createBarChart() {
		this.bars = new Chart(this.barChart.nativeElement, {
			type: 'bar',
			data: {
				labels: this.axis.x,
				datasets: [
					{
						label: 'Devices sold',
						data: this.axis.y,
						backgroundColor: 'rgb(38, 194, 129)', // array should have same number of elements as number of dataset
						borderColor: 'rgb(38, 194, 129)', // array should have same number of elements as number of dataset
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					yAxes: [
						{
							ticks: {
								beginAtZero: true
							}
						}
					]
				}
			}
		});
	}
}
