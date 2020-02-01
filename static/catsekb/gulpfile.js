"use strict"

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    gulpCopy = require('gulp-copy'),
    wait = require('gulp-wait'),
    concat = require('gulp-concat'),
    cssnano = require('gulp-cssnano'),
    del = require('del'),
    autoprefixer = require('gulp-autoprefixer'),
    uglify = require('gulp-uglifyjs'),
    imagemin = require('gulp-imagemin'),
    pngquant = require('imagemin-pngquant'),
    cache = require('gulp-cache'),
    gcmq = require('gulp-group-css-media-queries');

gulp.task('copy-bootstrap', function () {
    return gulp.src(['app/css/a.bootstrap.css'])
        .pipe((gulpCopy('dist/native_css/', {'prefix': 2})))
});

gulp.task('scss', ['copy-bootstrap'], function () {
    return gulp.src('app/sass/*.scss')
        .pipe(wait(500)) // !!!
        .pipe(sass())
        .pipe(gcmq())
        .pipe(autoprefixer(['last 15 versions', '> 1%'], { cascade: false }))
        .pipe(gulp.dest('dist/native_css'))
});

gulp.task('css-libs', ['scss'], function () {
    return gulp.src('dist/native_css/*.css')
        .pipe(cssnano({ zindex: false }))
        .pipe(concat('base.min.css'))
        .pipe(gulp.dest('dist/css/'));
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
