<script lang="ts">
	import feather from 'feather-icons/dist/feather.js';

	export let icon: string;
	export let size: string = '24px';
	export let stroke_width: string = '2';
	export let color: string = '#FFF';
	export let fill_color: string = 'none';
	export let settings: object = {};
	export let hover_icon: string = '';
	export let hover_color: string = '';
	export let hover_size: string = '';
	export let hover_fill_color: string = 'none';
	export let hover_stroke_width: number = 2;
	export let hovering: boolean = false;
	export let spin: boolean = false;
	export let spin_on_hover: boolean = false;
	export let pulse: boolean = false;
	export let ping: boolean = false;
	export let onClick: any = () => {};
	let className: string = '';
	export { className as class };

	if (!color) {
		color = '#FFF';
	}

	if (!fill_color) {
		// if fill_color = '', then set it to default: none
		fill_color = 'none';
	}

	if (!hover_icon) {
		hover_icon = icon;
	}

	if (!hover_fill_color) {
		hover_fill_color = 'none';
	}

	if (fill_color && (!hover_fill_color || hover_fill_color === 'none')) {
		hover_fill_color = fill_color;
	}

	function giveSize() {
		let w;
		if (typeof window !== 'undefined') {
			w = window.innerWidth;
		}

		if (w < 640) {
			size = '16px';
		} else if (w < 768) {
			size = '24px';
		} else if (w < 1024) {
			size = '28px';
		} else if (w < 1280) {
			size = '32px';
		} else {
			size = '40px';
		}
	}

	let cssClasses: string[] = [];
	if (className) cssClasses.push(className);
	if (spin) cssClasses.push('animations');
	if (spin_on_hover) cssClasses.push('hover:animate-spin');
	if (pulse) cssClasses.push('animate-pulse');
	if (ping) cssClasses.push('animate-ping');

	let componentHovering: boolean = false;
	let iconSettings = JSON.parse(JSON.stringify(settings));
	iconSettings.color = color;
	iconSettings.fill = fill_color;
	iconSettings['stroke-width'] = stroke_width;

	if (size.length > 0) {
		iconSettings.width = size;
		iconSettings.height = size;
	}

	const iconHoverColor = hover_color ? hover_color : color;

	function createSVG(icon: string, settings: object) {
		let svg = '';
		if (feather.icons[icon]) {
			svg = feather.icons[icon].toSvg(settings);
		} else {
			svg = feather.icons['help-circle'].toSvg(settings);
		}

		return svg;
	}

	let svg = createSVG(icon, iconSettings);

	function changeToHoverState() {
		componentHovering = true;
		onHover();
	}

	function onHover() {
		iconSettings.width = hover_size;
		iconSettings.height = hover_size;
		iconSettings.color = iconHoverColor;
		iconSettings.fill = hover_fill_color;
		iconSettings['stroke-width'] = hover_stroke_width;
		svg = createSVG(hover_icon, iconSettings);
	}

	function changeToNoHoverState() {
		componentHovering = false;
		onDehover();
	}

	function onDehover() {
		iconSettings.width = size;
		iconSettings.height = size;
		iconSettings.color = color;
		iconSettings.fill = fill_color;
		iconSettings['stroke-width'] = stroke_width;
		svg = createSVG(icon, iconSettings);
	}

	$: {
		giveSize();

		if (!hover_size) {
			hover_size = size;
		}

		if (hovering || componentHovering) onHover();
		else onDehover();

		if (icon) {
			hover_icon = icon;
			if (hovering || componentHovering) onHover();
			else onDehover();
		}

		if (stroke_width) {
			iconSettings['stroke-width'] = stroke_width;
			if (!hovering && !componentHovering) svg = createSVG(icon, iconSettings);
		}

		if (color) {
			iconSettings.color = color;
			if (!hovering && !componentHovering) svg = createSVG(icon, iconSettings);
		}

		if (fill_color) {
			iconSettings.fill = fill_color;
			if (!hovering && !componentHovering) svg = createSVG(icon, iconSettings);
		}

		if (hover_color) {
			iconSettings.color = hover_color;
			if (hovering && componentHovering) svg = createSVG(icon, iconSettings);
		}

		if (hover_fill_color) {
			iconSettings.fill = hover_fill_color;
			if (hovering && componentHovering) svg = createSVG(icon, iconSettings);
		}
	}
</script>

<div
	on:click={onClick}
	on:mouseenter={changeToHoverState}
	on:mouseleave={changeToNoHoverState}
	class={cssClasses.join(' ')}
	id="icondiv"
>
	{@html svg}
</div>

<style lang="postcss">
	.animations {
		animation: spin 1s linear infinite, pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
	}
</style>
