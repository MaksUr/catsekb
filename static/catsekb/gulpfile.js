var gulp 		 = require('gulp'), // Подключаем Gulp
    sass 		 = require('gulp-sass'); // Подключаем Sass пакет
    autoprefixer = require('gulp-autoprefixer'); // Подключаем библиотеку для автоматического добавления префиксов
    cssnano      = require('gulp-cssnano'), // Подключаем пакет для минификации CSS
    rename       = require('gulp-rename'); // Подключаем библиотеку для переименования файлов
    del          = require('del'); // Подключаем библиотеку для удаления файлов и папок

gulp.task('sass', function() { // Создаем таск "sass"
  return gulp.src(['app/sass/**/*.sass', 'app/sass/**/*.scss']) // Берем источник
    .pipe(sass()) // Преобразуем Sass в CSS посредством gulp-sass
    .pipe(autoprefixer(['last 15 versions', '> 1%', 'ie 8', 'ie 7'], { cascade: true }))
  });

gulp.task('clean', function() {
    return del.sync('dist'); // Удаляем папку dist перед сборкой
});

gulp.task('css-libs', ['sass'], function() {
    return gulp.src('app/css/*.css') // Выбираем файл для минификации
        .pipe(cssnano()) // Сжимаем
        .pipe(rename({suffix: '.min'})) // Добавляем суффикс .min
        .pipe(gulp.dest('app/css/min')); // Выгружаем в папку app/css
});

gulp.task('watch', function() {
  gulp.watch(['app/sass/**/*.sass', 'app/sass/**/*.scss'], ['sass']); // Наблюдение за sass файлами в папке sass
});

gulp.task('default', ['watch']);

gulp.task('build', ['clean', 'css-libs'], function() {

    var buildCss = gulp.src([ // Переносим библиотеки в продакшен
        'app/css/bootstrap/bootstrap.min.css',
        'app/css/min/*.css'
        ])
    .pipe(gulp.dest('dist/css'))

    var buildFonts = gulp.src('app/fonts/**/*') // Переносим шрифты в продакшен
    .pipe(gulp.dest('dist/fonts'))

    var buildJs = gulp.src('app/js/**/*') // Переносим скрипты в продакшен
    .pipe(gulp.dest('dist/js'))

    var buildImg = gulp.src('app/img/**/*') // Переносим img в продакшен
    .pipe(gulp.dest('dist/img'));

});