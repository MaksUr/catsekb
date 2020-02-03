FROM node:11

WORKDIR /front
COPY package.json .
COPY yarn.lock .
RUN yarn
COPY gulpfile.js ./gulpfile.js 
COPY app ./app
RUN node node_modules/gulp/bin/gulp.js build
#RUN cp -r /front/dist /dist/
#
FROM busybox
WORKDIR /dist

COPY --from=0 /front/dist/ .
