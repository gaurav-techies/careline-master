module.exports = function(grunt) {
    // Project configuration.
        grunt.initConfig({
            watch: {
                src: {
                    files: ['**/*.scss'],
                    tasks: ['compass:dev']
                },
                options: {
                    livereload: false
                }
            },
            compass: {
                dev: {
                    options: {
                        sassDir: 'carelineapp/src/scss',
                        cssDir: 'carelineapp/assets/carelineapp/css',
                        imagesPath: 'carelineapp/assets/carelineapp/images',
                        noLineComments: false,
                        outputStyle: 'compressed',
                        sourcemap: true
                    }
                }
            },
            cssmin: {
                target: {
                    files: [{
                        expand: true,
                        cwd: 'carelineapp/assets/carelineapp/css',
                        src: ['*.css', '!*.min.css'],
                        dest: 'carelineapp/assets/carelineapp/css',
                        ext: '.min.css'
                    }]
                }
            },
            // postcss: {
            //     options: {
            //         map: true, // inline sourcemaps
            //
            //         // or For Dev Only
            //         map: {
            //             inline: false, // save all sourcemaps as separate files...
            //             annotation: 'assets/css/' // ...to the specified directory
            //         },
            //         processors: [
            //             require('pixrem')(), // add fallbacks for rem units
            //             require('autoprefixer')({browsers: 'last 2 versions'}), // add vendor prefixes
            //             require('cssnano')() // minify the result
            //         ]
            //     },
            //     dist: {
            //         src: 'assets/css/*.css'
            //     }
            // },
            concat: {
                target1: {
                    files: {
                        "carelineapp/build/scripts.js": [
                            "carelineapp/src/js/jquery.js",
                            "carelineapp/src/js/bootstrap/bootstrap.js",
                            "carelineapp/src/js/bootstrap-select.js",
                            "carelineapp/src/js/bootstrap3-typeahead.js",
                            "carelineapp/src/js/formvalidation-dist-v0.8.1/dist/js/formValidation.js",
                            "carelineapp/src/js/formvalidation-dist-v0.8.1/dist/js/framework/bootstrap.js",
                            "carelineapp/src/js/intl-tel-input-11.0.12/build/js/intlTelInput.min.js",
                            "carelineapp/src/js/intl-tel-input-11.0.12/build/js/utils.js",
                            "carelineapp/src/js/custom-form.js",
                            "carelineapp/src/js/map.js",
                            "carelineapp/src/js/custom.js",
                            "carelineapp/src/js/blog_pagination.js",
                            "carelineapp/src/js/query-object.js",
                            "carelineapp/src/js/site-search-typehead.js",
                            "carelineapp/src/js/search-concat.js"
                        ]
                    }
                },
            },
            uglify: {
                target1: {
                    src: 'carelineapp/build/scripts.js',
                    dest: 'carelineapp/assets/carelineapp/js/scripts.min.js'
                },
            },
    
            compress: {
                main: {
                    options: {
                        mode: 'gzip'
                    },
                    // Each of the files in the src/ folder will be output to
                    // the dist/ folder each with the extension .gz.js
                    files: [{
                        expand: true,
                        src: [
                            'carelineapp/assets/carelineapp/css/styles.min.css',
                            'carelineapp/assets/carelineapp/js/scripts.min.js'
                        ],
                        dest: 'dist/'
                    }]
                }
            },
            shell: {
                  multiple: {
                    command: [
                            '~/.virtualenvs/carelineapp/bin/python /var/www/carelineapp/manage.py collectstatic --clear --noinput',
                            '~/.virtualenvs/carelineapp/bin/python /var/www/carelineapp/manage.py runsslserver 0.0.0.0:8000'
                    ].join('&&')
                  }
                }
            });
    
        grunt.loadNpmTasks('grunt-contrib-compass');
        grunt.loadNpmTasks('grunt-contrib-sass');
        // grunt.loadNpmTasks('grunt-postcss');
        // grunt.loadNpmTasks('grunt-pixrem');
        grunt.loadNpmTasks('grunt-contrib-concat');
        grunt.loadNpmTasks('grunt-contrib-watch');
        grunt.loadNpmTasks('grunt-contrib-uglify');
        grunt.loadNpmTasks('grunt-contrib-cssmin');
        grunt.loadNpmTasks('grunt-exec');
        grunt.loadNpmTasks('grunt-shell');
    
        // Define the default task
        grunt.registerTask('default', ['compass:dev','cssmin','concat','uglify','shell']);
    };