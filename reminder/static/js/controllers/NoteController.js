var NoteController = function($http) {
    var that = this;

    this.colors = '';
    this.tags = '';
    this.categories = '';
    this.notes = '';
    this.images = '';

    // USER's Actions
    this.user = {
        id: document.getElementById('user_id').textContent, // BAD WAY =(
        categories: [],
        tags: [],
        notes: [],
        images: []
    };

    // CATEGORY
    this.category = {
        id: '',
        url: '/categories/',
        data: {
            name: '',
            author: that.user.id,
        },
        helpText: {
            action: 'Create Category',
        },
        actions: {
            get: function() {
                $http.get(that.category.url).success(function(data) {that.categories = data;});
            },
            post: function() {
                $http.post(that.category.url, that.category.data).success(
                    function(data) {
                        that.category.actions.clear();
                        that.refreshPage();
                    });
            },
            put: function(id) {
                $http.put(that.category.url + id + '/', that.category.data).success(
                    function() {
                        that.category.actions.clear();
                        that.refreshPage();
                    });
            },
            delete: function(id) {
                $http.delete(that.category.url + id + '/').success(
                    function() {
                        that.category.actions.clear();
                        that.refreshPage();
                    });
            },
            deleteCats: function() {
                if (confirm('Do you really want to delete?')) {
                    for (var i = 0; i < that.user.categories.length; i++) {
                        that.category.actions.delete(that.user.categories[i]);
                    };
                };
            },
            set: function(id, name) {
                that.category.id = id;
                that.category.data.name = name;
                that.category.helpText.action = 'Change Category ' + id;
            },
            clear: function() {
                that.category.id = '';
                that.category.data.name = '';
                that.category.helpText.action = 'Create Category';
            },
        }
    };

    // TAG
    this.tag = {
        id: '',
        url: '/tags/',
        data: {
            name: '',
            author: that.user.id,
        },
        helpText: {
            action: 'Create tag',
        },
        actions: {
            get: function() {
                $http.get(that.tag.url).success(function(data) {that.tags = data;});
            },
            post: function() {
                $http.post(that.tag.url, that.tag.data).success(
                    function(data) {
                        that.refreshPage();
                        that.tag.actions.clear();
                    });
            },
            put: function(id) {
                $http.put(that.tag.url + id + '/', that.tag.data).success(
                    function() {
                        that.refreshPage();
                        that.tag.actions.clear();
                    });
            },
            delete: function(id) {
                $http.delete(that.tag.url + id + '/').success(function() {
                    that.refreshPage();
                    that.tag.actions.clear();
                });
            },
            deleteTags: function() {
                if (confirm('Do you really want to delete?')) {
                    for (var i = 0; i < that.user.tags.length; i++) {
                        that.tag.actions.delete(that.user.tags[i]);
                    };
                };
            },
            set: function(id, name) {
                that.tag.id = id;
                that.tag.data.name = name;
                that.tag.helpText.action = 'Change tag ' + id;
            },
            clear: function() {
                that.tag.id = '';
                that.tag.data.name = '';
                that.tag.helpText.action = 'Create tag';
            },
        }
    };

    // NOTE
    this.note = {
        id: '',
        url: '/notes/',
        data: {
            author: that.user.id,
            title: '',
            context: '',
            color: '',
            tag: [],
            category: [],
            image: []
        },
        helpText: {
            action: 'Create Note',
        },
        actions: {
            get: function() {
                $http.get(that.note.url).success(function(data) {that.notes = data;});
            },
            post: function() {
                $http.post(that.note.url, that.note.data).success(
                    function(data) {
                        that.refreshPage();
                        that.note.actions.clear();
                    });
            },
            put: function(id) {
                $http.put(that.note.url + id + '/', that.note.data).success(
                    function() {
                        that.refreshPage();
                        that.note.actions.clear();
                    });
            },
            delete: function(id) {
                $http.delete(that.note.url + id + '/').success(
                    function() {
                        that.refreshPage();
                        that.note.actions.clear();
                    });
            },
            deleteNots: function() {
                if (confirm('Do you really want to delete?')) {
                    for (var i = 0; i < that.user.notes.length; i++) {
                        that.note.actions.delete(that.user.notes[i]);
                    };
                };
            },
            set: function(data) {
                that.note.id = data.id;
                that.note.data.title = data.title;
                that.note.data.context = data.context;
                that.note.data.color = data.color;
                that.note.data.tag = data.tag;
                that.note.data.category = data.category;
                that.note.data.image = data.image;
                that.note.helpText.action = 'Change Note ' + data.id;
            },
            clear: function() {
                that.note.id = '';
                that.note.data.title = '';
                that.note.data.context = '';
                that.note.data.color = '';
                that.note.data.tag = [];
                that.note.data.category = [];
                that.note.data.image = [];
                that.note.helpText.action = 'Create Note';
            },
        }
    };

    // IMAGES
    this.image = {
        id: '',
        url: '/images/',
        data: {
            title: '',
            file: ''
        },
        actions: {
            get: function() {
                $http.get(that.image.url).success(function(data) {that.images = data;});
            },
            post: function(){
                var fd = new FormData();
                datas = $("#FormId").serializeArray();
                // send other data in the form
                for (var i = 0; i < datas.length; i++) {
                    fd.append(datas[i].name, datas[i].value);
                }
                // append file to FormData
                fd.append("select_file", $("#id_select_file")[0].files[0])
                // for sending manual values
                fd.append("type", "edit");
                url = that.image.url;

                $http.post(url, fd, {
                    headers: {'Content-Type': undefined },
                    transformRequest: angular.identity
                }).success(function(data, status, headers, config) {
                    that.refreshPage();
                    that.image.actions.clear()
                    $('#id_select_file').val(null);
                })
            },
            delete: function(id) {
                $http.delete(that.image.url + id + '/').success(function() {
                    that.image.actions.get();
                });
            },
            deleteImages: function() {
                if (confirm('Do you really want to delete?')) {
                    for (var i = 0; i < that.user.images.length; i++) {
                        that.image.actions.delete(that.user.images[i]);
                    };
                };
            },
            clear: function() {
                that.image.data.title = '',
                that.image.data.file = ''
            },
        }
    };

    this.refreshPage = function() {
        this.tag.actions.get();
        this.category.actions.get();
        this.note.actions.get();
        this.image.actions.get();
    };

    $http.get('/colors/').success(function(data) {that.colors = data;});
    this.refreshPage();

    this.getObj = function(id, where) {
        for (var i = 0; i < where.length; i++) {
            if (where[i].id == id) {
                return where[i];
            };
        };
    };

};
