var gulp = require('gulp');
var cssnano = require('gulp-cssnano');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var imagemin = require('gulp-imagemin');
var bs = require('browser-sync').create();
var util = require('gulp-util');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('greet',function(){
	console.log('hallo word!');
});

var path = {
    'html':'./templates/**/',
    'css':'./source/css/**/',
    'js':'./source/js/',
    'images':'./source/images/',
    'css_district':'./district/css/',
    'js_district':'./district/js/',
    'images_district':'./district/images/'
};

// 未加也可以.pipe(bs.stream())

// html处理
gulp.task('html',function(){
    gulp.src(path.html+'*.html')
        .pipe(bs.stream())
});


gulp.task('css',function(){
    console.log('css');
    gulp.src(path.css+'*.scss')
        .pipe(sass().on("error",sass.logError))
        .pipe(cssnano())
        .pipe(rename({'suffix':'.min'}))
        .pipe(gulp.dest(path.css_district))
        .pipe(bs.stream())
});


gulp.task('js',function(){
    gulp.src(path.js+'*.js')
        .pipe(sourcemaps.init())
        .pipe(uglify().on('error',util.log))
        .pipe(rename({'suffix':'.min'}))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.js_district))
        .pipe(bs.stream())
});





// 图片处理
gulp.task('images',function(){
    gulp.src(path.images+'*.*')
        .pipe(cache(imagemin()))
        .pipe(gulp.dest(path.images_district))
});

// 监听
gulp.task('watch',function(){
    console.log('watch');
    gulp.watch(path.html+'*.html',['html']);
    gulp.watch(path.css+'*.scss',['css']);
    gulp.watch(path.js+'*.js',['js']);
    gulp.watch(path.images+'*.*',['images']);
});

// initial 浏览器同步,// 加载bs:
// gulp.task('bs',function(){
//     bs.init({
//         'server':{'baseDir':'./'}
//     });
// });

// 换一个
gulp.task('bs',function(){
    bs.init({
        'proxy':'http://127.0.0.1:8000/'
    });
});


// 循环任务
gulp.task('default',['bs','watch']);