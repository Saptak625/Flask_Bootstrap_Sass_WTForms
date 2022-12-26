from flask_assets import Bundle

bundles = {
    'home_js': Bundle(
        # '../node_modules/bootstap/dist/js/bootstrap.min.js',
        'js/main.js',
        filters='jsmin',
        output='gen/packed.%(version)s.js'),
    'home_css': Bundle(
        'css/main.scss',
        filters='libsass',
        depends='css/**/*.scss',
        output='gen/packed.%(version)s.css')
}