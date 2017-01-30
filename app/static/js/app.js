Vue.component('one-list', {
    props: ['item'],
    template: '#template-one'
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
