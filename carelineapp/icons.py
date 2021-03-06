from wagtail.core.blocks import ChoiceBlock

class IconChoiceBlock(ChoiceBlock):
	choices = [
		('address-book', 'address-book'),
		('address-book-o', 'address-book-o'),
		('address-card', 'address-card'),
		('address-card-o', 'address-card-o'),
		('adjust', 'adjust'),
		('american-sign-language-interpreting', 'american-sign-language-interpreting'),
		('anchor', 'anchor'),
		('archive', 'archive'),
		('area-chart', 'area-chart'),
		('arrows', 'arrows'),
		('arrows-h', 'arrows-h'),
		('arrows-v', 'arrows-v'),
		('asl-interpreting ', 'asl-interpreting '),
		('assistive-listening-systems', 'assistive-listening-systems'),
		('asterisk', 'asterisk'),
		('at', 'at'),
		('audio-description', 'audio-description'),
		('automobile ', 'automobile '),
		('balance-scale', 'balance-scale'),
		('ban', 'ban'),
		('bank ', 'bank '),
		('bar-chart', 'bar-chart'),
		('bar-chart-o ', 'bar-chart-o '),
		('barcode', 'barcode'),
		('bars', 'bars'),
		('bath', 'bath'),
		('bathtub ', 'bathtub '),
		('battery ', 'battery '),
		('battery-0 ', 'battery-0 '),
		('battery-1 ', 'battery-1 '),
		('battery-2 ', 'battery-2 '),
		('battery-3 ', 'battery-3 '),
		('battery-4 ', 'battery-4 '),
		('battery-empty', 'battery-empty'),
		('battery-full', 'battery-full'),
		('battery-half', 'battery-half'),
		('battery-quarter', 'battery-quarter'),
		('battery-three-quarters', 'battery-three-quarters'),
		('bed', 'bed'),
		('beer', 'beer'),
		('bell', 'bell'),
		('bell-o', 'bell-o'),
		('bell-slash', 'bell-slash'),
		('bell-slash-o', 'bell-slash-o'),
		('bicycle', 'bicycle'),
		('binoculars', 'binoculars'),
		('birthday-cake', 'birthday-cake'),
		('blind', 'blind'),
		('bluetooth', 'bluetooth'),
		('bluetooth-b', 'bluetooth-b'),
		('bolt', 'bolt'),
		('bomb', 'bomb'),
		('book', 'book'),
		('bookmark', 'bookmark'),
		('bookmark-o', 'bookmark-o'),
		('braille', 'braille'),
		('briefcase', 'briefcase'),
		('bug', 'bug'),
		('building', 'building'),
		('building-o', 'building-o'),
		('bullhorn', 'bullhorn'),
		('bullseye', 'bullseye'),
		('bus', 'bus'),
		('cab ', 'cab '),
		('calculator', 'calculator'),
		('calendar', 'calendar'),
		('calendar-check-o', 'calendar-check-o'),
		('calendar-minus-o', 'calendar-minus-o'),
		('calendar-o', 'calendar-o'),
		('calendar-plus-o', 'calendar-plus-o'),
		('calendar-times-o', 'calendar-times-o'),
		('camera', 'camera'),
		('camera-retro', 'camera-retro'),
		('car', 'car'),
		('caret-square-o-down', 'caret-square-o-down'),
		('caret-square-o-left', 'caret-square-o-left'),
		('caret-square-o-right', 'caret-square-o-right'),
		('caret-square-o-up', 'caret-square-o-up'),
		('cart-arrow-down', 'cart-arrow-down'),
		('cart-plus', 'cart-plus'),
		('cc', 'cc'),
		('certificate', 'certificate'),
		('check', 'check'),
		('check-circle', 'check-circle'),
		('check-circle-o', 'check-circle-o'),
		('check-square', 'check-square'),
		('check-square-o', 'check-square-o'),
		('child', 'child'),
		('circle', 'circle'),
		('circle-o', 'circle-o'),
		('circle-o-notch', 'circle-o-notch'),
		('circle-thin', 'circle-thin'),
		('clock-o', 'clock-o'),
		('clone', 'clone'),
		('close ', 'close '),
		('cloud', 'cloud'),
		('cloud-download', 'cloud-download'),
		('cloud-upload', 'cloud-upload'),
		('code', 'code'),
		('code-fork', 'code-fork'),
		('coffee', 'coffee'),
		('cog', 'cog'),
		('cogs', 'cogs'),
		('comment', 'comment'),
		('comment-o', 'comment-o'),
		('commenting', 'commenting'),
		('commenting-o', 'commenting-o'),
		('comments', 'comments'),
		('comments-o', 'comments-o'),
		('compass', 'compass'),
		('copyright', 'copyright'),
		('creative-commons', 'creative-commons'),
		('credit-card', 'credit-card'),
		('credit-card-alt', 'credit-card-alt'),
		('crop', 'crop'),
		('crosshairs', 'crosshairs'),
		('cube', 'cube'),
		('cubes', 'cubes'),
		('cutlery', 'cutlery'),
		('dashboard ', 'dashboard '),
		('database', 'database'),
		('deaf', 'deaf'),
		('deafness ', 'deafness '),
		('desktop', 'desktop'),
		('diamond', 'diamond'),
		('dot-circle-o', 'dot-circle-o'),
		('download', 'download'),
		('drivers-license ', 'drivers-license '),
		('drivers-license-o ', 'drivers-license-o '),
		('edit ', 'edit '),
		('ellipsis-h', 'ellipsis-h'),
		('ellipsis-v', 'ellipsis-v'),
		('envelope', 'envelope'),
		('envelope-o', 'envelope-o'),
		('envelope-open', 'envelope-open'),
		('envelope-open-o', 'envelope-open-o'),
		('envelope-square', 'envelope-square'),
		('eraser', 'eraser'),
		('exchange', 'exchange'),
		('exclamation', 'exclamation'),
		('exclamation-circle', 'exclamation-circle'),
		('exclamation-triangle', 'exclamation-triangle'),
		('external-link', 'external-link'),
		('external-link-square', 'external-link-square'),
		('eye', 'eye'),
		('eye-slash', 'eye-slash'),
		('eyedropper', 'eyedropper'),
		('fax', 'fax'),
		('feed ', 'feed '),
		('female', 'female'),
		('fighter-jet', 'fighter-jet'),
		('file-archive-o', 'file-archive-o'),
		('file-audio-o', 'file-audio-o'),
		('file-code-o', 'file-code-o'),
		('file-excel-o', 'file-excel-o'),
		('file-image-o', 'file-image-o'),
		('file-movie-o ', 'file-movie-o '),
		('file-pdf-o', 'file-pdf-o'),
		('file-photo-o ', 'file-photo-o '),
		('file-picture-o ', 'file-picture-o '),
		('file-powerpoint-o', 'file-powerpoint-o'),
		('file-sound-o ', 'file-sound-o '),
		('file-video-o', 'file-video-o'),
		('file-word-o', 'file-word-o'),
		('file-zip-o ', 'file-zip-o '),
		('film', 'film'),
		('filter', 'filter'),
		('fire', 'fire'),
		('fire-extinguisher', 'fire-extinguisher'),
		('flag', 'flag'),
		('flag-checkered', 'flag-checkered'),
		('flag-o', 'flag-o'),
		('flash ', 'flash '),
		('flask', 'flask'),
		('folder', 'folder'),
		('folder-o', 'folder-o'),
		('folder-open', 'folder-open'),
		('folder-open-o', 'folder-open-o'),
		('frown-o', 'frown-o'),
		('futbol-o', 'futbol-o'),
		('gamepad', 'gamepad'),
		('gavel', 'gavel'),
		('gear ', 'gear '),
		('gears ', 'gears '),
		('gift', 'gift'),
		('glass', 'glass'),
		('globe', 'globe'),
		('graduation-cap', 'graduation-cap'),
		('group ', 'group '),
		('hand-grab-o ', 'hand-grab-o '),
		('hand-lizard-o', 'hand-lizard-o'),
		('hand-paper-o', 'hand-paper-o'),
		('hand-peace-o', 'hand-peace-o'),
		('hand-pointer-o', 'hand-pointer-o'),
		('hand-rock-o', 'hand-rock-o'),
		('hand-scissors-o', 'hand-scissors-o'),
		('hand-spock-o', 'hand-spock-o'),
		('hand-stop-o ', 'hand-stop-o '),
		('handshake-o', 'handshake-o'),
		('hard-of-hearing ', 'hard-of-hearing '),
		('hashtag', 'hashtag'),
		('hdd-o', 'hdd-o'),
		('headphones', 'headphones'),
		('heart', 'heart'),
		('heart-o', 'heart-o'),
		('heartbeat', 'heartbeat'),
		('history', 'history'),
		('home', 'home'),
		('hotel ', 'hotel '),
		('hourglass', 'hourglass'),
		('hourglass-1 ', 'hourglass-1 '),
		('hourglass-2 ', 'hourglass-2 '),
		('hourglass-3 ', 'hourglass-3 '),
		('hourglass-end', 'hourglass-end'),
		('hourglass-half', 'hourglass-half'),
		('hourglass-o', 'hourglass-o'),
		('hourglass-start', 'hourglass-start'),
		('i-cursor', 'i-cursor'),
		('id-badge', 'id-badge'),
		('id-card', 'id-card'),
		('id-card-o', 'id-card-o'),
		('image ', 'image '),
		('inbox', 'inbox'),
		('industry', 'industry'),
		('info', 'info'),
		('info-circle', 'info-circle'),
		('institution ', 'institution '),
		('key', 'key'),
		('keyboard-o', 'keyboard-o'),
		('language', 'language'),
		('laptop', 'laptop'),
		('leaf', 'leaf'),
		('legal ', 'legal '),
		('lemon-o', 'lemon-o'),
		('level-down', 'level-down'),
		('level-up', 'level-up'),
		('life-bouy ', 'life-bouy '),
		('life-buoy ', 'life-buoy '),
		('life-ring', 'life-ring'),
		('life-saver ', 'life-saver '),
		('lightbulb-o', 'lightbulb-o'),
		('line-chart', 'line-chart'),
		('location-arrow', 'location-arrow'),
		('lock', 'lock'),
		('low-vision', 'low-vision'),
		('magic', 'magic'),
		('magnet', 'magnet'),
		('mail-forward ', 'mail-forward '),
		('mail-reply ', 'mail-reply '),
		('mail-reply-all ', 'mail-reply-all '),
		('male', 'male'),
		('map', 'map'),
		('map-marker', 'map-marker'),
		('map-o', 'map-o'),
		('map-pin', 'map-pin'),
		('map-signs', 'map-signs'),
		('meh-o', 'meh-o'),
		('microchip', 'microchip'),
		('microphone', 'microphone'),
		('microphone-slash', 'microphone-slash'),
		('minus', 'minus'),
		('minus-circle', 'minus-circle'),
		('minus-square', 'minus-square'),
		('minus-square-o', 'minus-square-o'),
		('mobile', 'mobile'),
		('mobile-phone ', 'mobile-phone '),
		('money', 'money'),
		('moon-o', 'moon-o'),
		('mortar-board ', 'mortar-board '),
		('motorcycle', 'motorcycle'),
		('mouse-pointer', 'mouse-pointer'),
		('music', 'music'),
		('navicon ', 'navicon '),
		('newspaper-o', 'newspaper-o'),
		('object-group', 'object-group'),
		('object-ungroup', 'object-ungroup'),
		('paint-brush', 'paint-brush'),
		('paper-plane', 'paper-plane'),
		('paper-plane-o', 'paper-plane-o'),
		('paw', 'paw'),
		('pencil', 'pencil'),
		('pencil-square', 'pencil-square'),
		('pencil-square-o', 'pencil-square-o'),
		('percent', 'percent'),
		('phone', 'phone'),
		('phone-square', 'phone-square'),
		('photo ', 'photo '),
		('picture-o', 'picture-o'),
		('pie-chart', 'pie-chart'),
		('plane', 'plane'),
		('plug', 'plug'),
		('plus', 'plus'),
		('plus-circle', 'plus-circle'),
		('plus-square', 'plus-square'),
		('plus-square-o', 'plus-square-o'),
		('podcast', 'podcast'),
		('power-off', 'power-off'),
		('print', 'print'),
		('puzzle-piece', 'puzzle-piece'),
		('qrcode', 'qrcode'),
		('question', 'question'),
		('question-circle', 'question-circle'),
		('question-circle-o', 'question-circle-o'),
		('quote-left', 'quote-left'),
		('quote-right', 'quote-right'),
		('random', 'random'),
		('recycle', 'recycle'),
		('refresh', 'refresh'),
		('registered', 'registered'),
		('remove ', 'remove '),
		('reorder ', 'reorder '),
		('reply', 'reply'),
		('reply-all', 'reply-all'),
		('retweet', 'retweet'),
		('road', 'road'),
		('rocket', 'rocket'),
		('rss', 'rss'),
		('rss-square', 'rss-square'),
		('s15 ', 's15 '),
		('search', 'search'),
		('search-minus', 'search-minus'),
		('search-plus', 'search-plus'),
		('send ', 'send '),
		('send-o ', 'send-o '),
		('server', 'server'),
		('share', 'share'),
		('share-alt', 'share-alt'),
		('share-alt-square', 'share-alt-square'),
		('share-square', 'share-square'),
		('share-square-o', 'share-square-o'),
		('shield', 'shield'),
		('ship', 'ship'),
		('shopping-bag', 'shopping-bag'),
		('shopping-basket', 'shopping-basket'),
		('shopping-cart', 'shopping-cart'),
		('shower', 'shower'),
		('sign-in', 'sign-in'),
		('sign-language', 'sign-language'),
		('sign-out', 'sign-out'),
		('signal', 'signal'),
		('signing ', 'signing '),
		('sitemap', 'sitemap'),
		('sliders', 'sliders'),
		('smile-o', 'smile-o'),
		('snowflake-o', 'snowflake-o'),
		('soccer-ball-o ', 'soccer-ball-o '),
		('sort', 'sort'),
		('sort-alpha-asc', 'sort-alpha-asc'),
		('sort-alpha-desc', 'sort-alpha-desc'),
		('sort-amount-asc', 'sort-amount-asc'),
		('sort-amount-desc', 'sort-amount-desc'),
		('sort-asc', 'sort-asc'),
		('sort-desc', 'sort-desc'),
		('sort-down ', 'sort-down '),
		('sort-numeric-asc', 'sort-numeric-asc'),
		('sort-numeric-desc', 'sort-numeric-desc'),
		('sort-up ', 'sort-up '),
		('space-shuttle', 'space-shuttle'),
		('spinner', 'spinner'),
		('spoon', 'spoon'),
		('square', 'square'),
		('square-o', 'square-o'),
		('star', 'star'),
		('star-half', 'star-half'),
		('star-half-empty ', 'star-half-empty '),
		('star-half-full ', 'star-half-full '),
		('star-half-o', 'star-half-o'),
		('star-o', 'star-o'),
		('sticky-note', 'sticky-note'),
		('sticky-note-o', 'sticky-note-o'),
		('street-view', 'street-view'),
		('suitcase', 'suitcase'),
		('sun-o', 'sun-o'),
		('support ', 'support '),
		('tablet', 'tablet'),
		('tachometer', 'tachometer'),
		('tag', 'tag'),
		('tags', 'tags'),
		('tasks', 'tasks'),
		('taxi', 'taxi'),
		('television', 'television'),
		('terminal', 'terminal'),
		('thermometer ', 'thermometer '),
		('thermometer-0 ', 'thermometer-0 '),
		('thermometer-1 ', 'thermometer-1 '),
		('thermometer-2 ', 'thermometer-2 '),
		('thermometer-3 ', 'thermometer-3 '),
		('thermometer-4 ', 'thermometer-4 '),
		('thermometer-empty', 'thermometer-empty'),
		('thermometer-full', 'thermometer-full'),
		('thermometer-half', 'thermometer-half'),
		('thermometer-quarter', 'thermometer-quarter'),
		('thermometer-three-quarters', 'thermometer-three-quarters'),
		('thumb-tack', 'thumb-tack'),
		('thumbs-down', 'thumbs-down'),
		('thumbs-o-down', 'thumbs-o-down'),
		('thumbs-o-up', 'thumbs-o-up'),
		('thumbs-up', 'thumbs-up'),
		('ticket', 'ticket'),
		('times', 'times'),
		('times-circle', 'times-circle'),
		('times-circle-o', 'times-circle-o'),
		('times-rectangle ', 'times-rectangle '),
		('times-rectangle-o ', 'times-rectangle-o '),
		('tint', 'tint'),
		('toggle-down ', 'toggle-down '),
		('toggle-left ', 'toggle-left '),
		('toggle-off', 'toggle-off'),
		('toggle-on', 'toggle-on'),
		('toggle-right ', 'toggle-right '),
		('toggle-up ', 'toggle-up '),
		('trademark', 'trademark'),
		('trash', 'trash'),
		('trash-o', 'trash-o'),
		('tree', 'tree'),
		('trophy', 'trophy'),
		('truck', 'truck'),
		('tty', 'tty'),
		('tv ', 'tv '),
		('umbrella', 'umbrella'),
		('universal-access', 'universal-access'),
		('university', 'university'),
		('unlock', 'unlock'),
		('unlock-alt', 'unlock-alt'),
		('unsorted ', 'unsorted '),
		('upload', 'upload'),
		('user', 'user'),
		('user-circle', 'user-circle'),
		('user-circle-o', 'user-circle-o'),
		('user-o', 'user-o'),
		('user-plus', 'user-plus'),
		('user-secret', 'user-secret'),
		('user-times', 'user-times'),
		('users', 'users'),
		('vcard ', 'vcard '),
		('vcard-o ', 'vcard-o '),
		('video-camera', 'video-camera'),
		('volume-control-phone', 'volume-control-phone'),
		('volume-down', 'volume-down'),
		('volume-off', 'volume-off'),
		('volume-up', 'volume-up'),
		('warning ', 'warning '),
		('wheelchair', 'wheelchair'),
		('wheelchair-alt', 'wheelchair-alt'),
		('wifi', 'wifi'),
		('window-close', 'window-close'),
		('window-close-o', 'window-close-o'),
		('window-maximize', 'window-maximize'),
		('window-minimize', 'window-minimize'),
		('window-restore', 'window-restore'),
		('wrench', 'wrench'),
	]