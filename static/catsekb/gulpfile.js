var gulp       = require('gulp'), // Подключаем Gulp
    sass         = require('gulp-sass'), //Подключаем Sass пакет,
    concatCss = require('gulp-concat-css'), // Подключаем gulp-concat (для конкатенации файлов)
    cssnano      = require('gulp-cssnano'), // Подключаем пакет для минификации CSS
    rename       = require('gulp-rename'), // Подключаем библиотеку для переименования файлов
    del          = require('del'), // Подключаем библиотеку для удаления файлов и папок
    autoprefixer = require('gulp-autoprefixer');// Подключаем библиотеку для автоматического добавления префиксов
    uglify      = require('gulp-uglifyjs'), // Подключаем gulp-uglifyjs (для сжатия JS)

gulp.task('sass', function(){ // Создаем таск Sass
    return gulp.src('app/sass/**/*') // Берем источник
        .pipe(sass()) // Преобразуем Sass в CSS посредством gulp-sass
        .pipe(autoprefixer(['last 16 versions', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'], { cascade: true })) // Создаем префиксы
        .pipe(gulp.dest('app/css')) // Выгружаем результата в папку app/css
});

gulp.task('css-libs', ['sass'], function() {
    return gulp.src('app/css/*.css') // Выбираем файл для минификации
        .pipe(cssnano({zindex: false})) // Сжимаем
        .pipe(rename({suffix: '.min'})) // Добавляем суффикс .min
        .pipe(gulp.dest('app/css/min')); // Выгружаем в папку app/css
});

gulp.task('concat', function () {
  return gulp.src('app/css/min/*.min')
    .pipe(concatCss('concat.css'))
    .pipe(gulp.dest('dist/css'));
});

gulp.task('scripts', function() {
    return gulp.src([ // Берем все необходимые библиотеки
        'app/js/script.js',
        'app/js/script_cats.js',
        'app/js/script_form.js'
        ])
        .pipe(uglify()) // Сжимаем JS файл
        .pipe(gulp.dest('app/js/min')); // Выгружаем в папку app/js
});

gulp.task('watch', ['css-libs'], function() {
    gulp.watch('app/sass/**/*.scss', ['sass']); // Наблюдение за sass файлами в папке sass
});

gulp.task('clean', function() {
    return del.sync('dist'); // Удаляем папку dist перед сборкой
});

gulp.task('build', ['clean', 'css-libs'], function() {

    var buildCss = gulp.src([ // Переносим библиотеки в продакшен
        'app/css/bootstrap/*.min.css',
        'app/css/min/*.css'
        ])
    .pipe(gulp.dest('dist/css'))

    var buildFonts = gulp.src('app/fonts/**/*') // Переносим шрифты в продакшен
    .pipe(gulp.dest('dist/fonts'))

    var buildJs = gulp.src('app/js/**/*') // Переносим скрипты в продакшен
    .pipe(gulp.dest('dist/js'))

    var buildImg = gulp.src('app/img/**/*') // Переносим шрифты в продакшен
    .pipe(gulp.dest('dist/img'))

});

gulp.task('default', ['watch']);