'use strict';

module.exports = function(grunt) {
    var css_path = 'controlcenter/static/controlcenter/css/',
        styl_path = 'controlcenter/stylus/',
        file_names = ['all', 'chartist-default-colors', 'chartist-material-colors'],
        files = {};

    for (var i = 0; i < file_names.length; i++){
        files[css_path + file_names[i] + '.css'] = styl_path + file_names[i] + '.styl';
    }

    grunt.initConfig({
        stylus: {
            build: {
                options: {
                    compress: false,
                    urlfunc: 'embedurl',
                    use: [
                        function(){
                            return require('autoprefixer-stylus')('last 2 versions');
                        }
                    ]
                },
                files: files
            }
        },

        clean: {
            dist: [css_path + '*.css']
        },

        watch: {
            css: {
                files: styl_path + '*.styl',
                tasks: ['stylus:build'],
                options: {
                    debounceDelay: 500
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.registerTask('default', ['clean', 'stylus']);
    grunt.registerTask('prod', ['clean', 'stylus']);
};