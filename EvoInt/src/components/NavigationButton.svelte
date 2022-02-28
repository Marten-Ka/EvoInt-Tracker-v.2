<script lang="ts">
	import { goto } from '$app/navigation';

	export let text: string;
	export let href: string;

	function onClick() {
		goto(href);
	}
</script>

<button on:click={onClick}>{text}</button>

<style lang="postcss">
	button {
		max-height: fit-content;
		height: fit-content;
		@apply p-2 border border-gray-900 rounded-md transition-all duration-150;
	}
	button:hover {
		@apply bg-opacity-50 scale-105;
	}
</style>
