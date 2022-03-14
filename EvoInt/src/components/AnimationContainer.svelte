<script lang="ts">
	import Saos from 'saos';

	export let from_right: boolean = false;
	export let time: string = '3s';
	export let delay: string = '0s';
	export let oneTimeDelay: boolean = true;

	function handleObserver() {
		if (oneTimeDelay) delay = '0s';
	}

	// animation: name duration (1s, 2s, 3s, ...) function (linear, cubic-bezier, ...) delay (1s, 2s, 3s, ...) iteration-count (1, 2, 3, infinite) direction (reverse, both, ...)
</script>

<Saos
	on:update={handleObserver}
	animation={`${
		from_right ? 'from-right' : 'from-left'
	} ${time} cubic-bezier(0, 0, 0.2, 1) ${delay} both`}
>
	<slot />
</Saos>

<style lang="postcss">
	@keyframes -global-from-left {
		0% {
			transform: translateX(-10vw);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
	@keyframes -global-from-right {
		0% {
			transform: translateX(10vw);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
</style>
