Vue.component('one-list', {
    props: ['item'],
    template: '#template-one'
});

var app_zero = new Vue({
    el: '#app-zero',
    data: {
        ts: {}
    },
    methods: {
        fetchData: function () {
            this.$http.get('/api/ts')
                .then(function (response) {
                    this.ts = response.data.now;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        setInterval(this.fetchData,
        1000);
    }
});

var app_one = new Vue({
    el: '#app-one',
    data: {
        one_list: []
    },
    methods: {
        fetchData: function () {
            this.$http.get('/api/one')
                .then(function (response) {
                    this.one_list = response.data.one;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        this.fetchData();
    }
});

var app_two = new Vue({
    el: '#app-two',
    data: {
        two_list: []
    },
    methods: {
        fetchData: function () {
            this.$http.get('/api/two')
                .then(function (response) {
                    this.two_list = response.data.two;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        this.fetchData();
    }
});
