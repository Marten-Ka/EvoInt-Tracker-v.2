<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let text: string;
	export let size: string;

	function onClick() {
		dispatch('click');
	}
</script>

<button on:click={onClick} class={'button-' + size}>{text}</button>

<style lang="postcss">
	.button-0 {
		background-color: rgb(175, 175, 175);
		border: none;
	}
	.button-1 {
		font-size: 2rem;
		background-color: rgb(175, 175, 175);
		border: none;
	}
	.button-2 {
		font-size: 2.5rem;
		background-color: rgb(175, 175, 175);
		border: none;
	}
</style>
