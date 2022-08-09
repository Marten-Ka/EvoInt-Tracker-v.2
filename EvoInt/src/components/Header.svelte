<script>
	import { goto } from '$app/navigation';
	import { browser } from '$app/env';
	import NavigationButton from './NavigationButton.svelte';

	function onHome() {
		goto('/');
	}

	let VIKUS_VIEWER_URL = '';
	if (browser) {
		VIKUS_VIEWER_URL = `${window.location.protocol}//${window.location.hostname}:8080/vikus_viewer`;
	}
</script>

<header>
	<img src="/logo.png" alt="EvoInt-Logo" width="159px" on:click={onHome} />
	<div class="flex flex-wrap" id="navigation">
		<NavigationButton text="Tutorial" href="/tutorial" />
		<NavigationButton text="Über uns" href="/about_us" />
		<NavigationButton text="Timeline" href="/timeline" />
		<NavigationButton text="Vikus-Viewer" href={VIKUS_VIEWER_URL} />
	</div>
</header>

<style lang="postcss">
	header {
		@apply font-evoint p-4 w-full flex items-center gap-2 sm:gap-5 bg-black text-gray-200;
	}

	img {
		@apply hover:cursor-pointer w-28 sm:w-32 md:w-36 lg:w-40;
	}

	#navigation {
		@apply flex gap-5 text-xs sm:text-sm md:text-base lg:text-base;
	}
</style>
