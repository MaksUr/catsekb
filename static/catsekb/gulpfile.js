"use strict"

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    wait = require('gulp-wait'),
    browserSync = require('browser-sync'),
    concat = require('gulp-concat'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    del = require('del'),
    autoprefixer = require('gulp-autoprefixer'),
    uglify = require('gulp-uglifyjs'),
    imagemin = require('gulp-imagemin'),
    pngquant = require('imagemin-pngquant'),
    cache = require('gulp-cache'),
    gcmq = require('gulp-group-css-media-queries');

gulp.task('scss', function () {
    return gulp.src('app/sass/*.scss')
        .pipe(wait(500)) // !!!
        .pipe(sass())
        .pipe(gcmq())
        .pipe(autoprefixer(['last 15 versions', '> 1%'], { cascade: false }))
        .pipe(gulp.dest('app/css'))
        .pipe(browserSync.reload({ stream: true }))
});

gulp.task('browser-sync', function () {
    browserSync({
        server: {
            baseDir: 'app'
        },
        notify: false
    });
});

gulp.task('css-libs', ['scss'], function () {
    return gulp.src('app/css/*.css')
        .pipe(cssnano({ zindex: false }))
        // .pipe(rename({suffix: '.min'}))
        .pipe(concat('base.min.css'))
        .pipe(gulp.dest('app/css/min'));
});

gulp.task('watch', ['css-libs', 'browsguer-sync'], function () {
    gulp.watch('app/sass/**/*.scss', ['scss']);
    gulp.watch('app/**/*.html', browserSync.reload);
    gulp.watch('app/js/**/*.js', browserSync.reload);
});

gulp.task('clean', function () {
    return del.sync('dist');
});

gulp.task('scripts', function () {
    return gulp.src('app/js/*.js')
        // .pipe(concat('script.js'))
        .pipe(uglify())
        .pipe(gulp.dest('app/js/min'));
});

gulp.task('img', function () {
    return gulp.src('app/img/**/*')
        .pipe(cache(imagemin({
            interlaced: true,
            progressive: true,
            svgoPlugins: [{ removeViewBox: false }],
            use: [pngquant()]
        })))
        .pipe(gulp.dest('dist/img'));
});

gulp.task('build', ['clean', 'img', 'css-libs'], function () {

    var buildCss = gulp.src([
        'app/css/min/*.css'
    ])
        .pipe(gulp.dest('dist/css'))

    var buildFonts = gulp.src('app/fonts/**/*')
        .pipe(gulp.dest('dist/fonts'))

    var buildJs = gulp.src('app/js/*')
        .pipe(gulp.dest('dist/js'))

    var buildHtml = gulp.src('app/**/*.html')
        .pipe(gulp.dest('dist'));

});

gulp.task('clear', function () {
    return cache.clearAll();
});

gulp.task('default', ['watch']);
