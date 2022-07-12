<script>
	import { goto } from '$app/navigation';

	import NavigationButton from './NavigationButton.svelte';

	function onHome() {
		goto('/');
	}
</script>

<header>
	<img src="../../static/Logo.png" alt="EvoInt-Logo" width="159px" on:click={onHome} />
	<div id="navigation">
		<NavigationButton text="Tutorial" href="/tutorial" />
		<NavigationButton text="Über uns" href="/about_us" />
		<NavigationButton text="Timeline" href="/timeline" />
	</div>
</header>

<style lang="postcss">
	header {
		@apply font-evoint p-4 w-full flex items-center gap-5 bg-black text-gray-200;
	}

	img {
		@apply hover:cursor-pointer;
	}

	#navigation {
		@apply flex gap-5;
	}
</style>
